---
type: section
subject: "[[Calculus]]"
chapter: 14
section: 92
stewart: "14.3"
aliases: ["Stewart 14.3"]
tags: [calculus, math233]
---
← [[§91 Limits and Continuity]] · ↑ [[· 14 Partial Derivatives]] · [[§93 Tangent Planes and Linear Approximations]] →

*Stewart, Section 14.3 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q24).*

A partial derivative is an ordinary derivative taken while all but one variable are held fixed. So nothing new is needed to compute one: $f_x$ is found by treating $y$ as a constant and differentiating with respect to $x$ by the rules of Chapter 3. Geometrically, $f_x(a, b)$ and $f_y(a, b)$ are the slopes of the curves in which the vertical planes $y = b$ and $x = a$ cut the graph of $f$; physically, they are rates of change in the coordinate directions. Differentiating again gives second partial derivatives, and Clairaut's Theorem says that the order of differentiation does not matter when the mixed partials are continuous. Partial derivatives are the language of the partial differential equations of physics, such as Laplace's equation and the wave equation.

## Partial Derivatives of Functions of Two Variables

The heat index $I = f(T, H)$ is the temperature that it feels like when the actual temperature is $T$ (°F) and the relative humidity is $H$ (%). Holding $H = 70$ fixed, $g(T) = f(T, 70)$ is a function of one variable, and its derivative $g'(96)$ is the rate at which $I$ increases with $T$ when $T = 96$ and $H = 70$. From the National Weather Service table, $\frac{f(98, 70) - f(96, 70)}{2} = \frac{133 - 125}{2} = 4$ and $\frac{f(94, 70) - f(96, 70)}{-2} = \frac{118 - 125}{-2} = 3.5$; the average, $3.75$, estimates $g'(96)$. Holding $T = 96$ fixed instead and varying $H$ gives $G(H) = f(96, H)$ and the estimate $G'(70) \approx \frac12 (1 + 0.8) = 0.9$. These are the partial derivatives $f_T(96, 70) \approx 3.75$ and $f_H(96, 70) \approx 0.9$.

> [!definition] Definition §92.1: Partial Derivatives at a Point
> Let $f$ be a function of two variables. If $g(x) = f(x, b)$ has a derivative at $a$, then this derivative is the **partial derivative of $f$ with respect to $x$ at $(a, b)$**, denoted $f_x(a, b)$:
>
> $$
> f_x(a, b) = g'(a) \quad\text{where } g(x) = f(x, b) . \qquad (1)
> $$
>
> By the definition of a derivative,
>
> $$
> f_x(a, b) = \lim_{h \to 0} \frac{f(a + h, b) - f(a, b)}{h} . \qquad (2)
> $$
>
> Similarly, the **partial derivative of $f$ with respect to $y$ at $(a, b)$** is obtained by keeping $x$ fixed ($x = a$) and finding the ordinary derivative at $b$ of $G(y) = f(a, y)$:
>
> $$
> f_y(a, b) = \lim_{h \to 0} \frac{f(a, b + h) - f(a, b)}{h} . \qquad (3)
> $$
>
> *Stewart: 14.3, Equations 1, 2 and 3*

^def-92-1

> [!definition] Definition §92.2: Partial Derivatives as Functions; Notation
> If $f$ is a function of two variables, its **partial derivatives** are the functions $f_x$ and $f_y$ defined by
>
> $$
> f_x(x, y) = \lim_{h \to 0} \frac{f(x + h, y) - f(x, y)}{h} , \qquad f_y(x, y) = \lim_{h \to 0} \frac{f(x, y + h) - f(x, y)}{h} .
> $$
>
> **Notation.** If $z = f(x, y)$, we write
>
> $$
> f_x(x, y) = f_x = \frac{\partial f}{\partial x} = \frac{\partial}{\partial x} f(x, y) = \frac{\partial z}{\partial x} = f_1 = D_1 f = D_x f ,
> $$
>
> $$
> f_y(x, y) = f_y = \frac{\partial f}{\partial y} = \frac{\partial}{\partial y} f(x, y) = \frac{\partial z}{\partial y} = f_2 = D_2 f = D_y f .
> $$
>
> The subscript $1$ in $f_1$, $D_1 f$ indicates differentiation with respect to the *first* variable. Unlike $dy/dx$, the symbol $\partial f / \partial x$ cannot be interpreted as a ratio of differentials.
>
> *Stewart: 14.3, Definition 4 and Notations for Partial Derivatives*

^def-92-2

> [!remark]- Connections
> - Rigorous treatment: [[§4 Partial Derivatives#^def-4-1|452 Def. §4.1]]. Partial derivatives can exist at a point where $f$ is not even continuous ([[§4 Partial Derivatives#^ex-4-1|452 Ex. §4.1]]; compare Example §91.1(b)); they only see the two lines through the point parallel to the axes. This is why §93 needs the stronger notion of differentiability, [[§93 Tangent Planes and Linear Approximations#^def-93-3|Definition §93.3]].

> [!theorem] Theorem §92.1: Rule for Finding Partial Derivatives
> If $z = f(x, y)$:
> 1. To find $f_x$, regard $y$ as a constant and differentiate $f(x, y)$ with respect to $x$.
> 2. To find $f_y$, regard $x$ as a constant and differentiate $f(x, y)$ with respect to $y$.
>
> *Stewart: 14.3, Rule for Finding Partial Derivatives of z = f(x, y)*

^thm-92-1

> [!proof]+ Proof
> By Equation (1), $f_x(a, b)$ is the ordinary derivative at $a$ of the function $g(x) = f(x, b)$ of one variable, in which $y = b$ is a constant. So $f_x$ is computed by the one-variable differentiation rules with $y$ treated as a constant. The same holds for $f_y$ with $G(y) = f(a, y)$.

^pf-92-1

*Uses:* [[§92 Partial Derivatives#^def-92-1|Def. §92.1]]

> [!example] Example §92.1: First and Second Partial Derivatives
> Let $f(x, y) = x^3 + x^2 y^3 - 2y^2$. Find $f_x(2, 1)$ and $f_y(2, 1)$, and all the second partial derivatives of $f$ ([[§92 Partial Derivatives#^def-92-4|Definition §92.4]]).
>
> **First partials.** Holding $y$ constant and differentiating with respect to $x$,
>
> $$
> f_x(x, y) = 3x^2 + 2xy^3 , \qquad f_x(2, 1) = 3 \cdot 2^2 + 2 \cdot 2 \cdot 1^3 = 16 .
> $$
>
> Holding $x$ constant and differentiating with respect to $y$,
>
> $$
> f_y(x, y) = 3x^2 y^2 - 4y , \qquad f_y(2, 1) = 3 \cdot 2^2 \cdot 1^2 - 4 \cdot 1 = 8 .
> $$
>
> **Second partials.**
>
> $$
> \begin{aligned}
> f_{xx} &= \frac{\partial}{\partial x}(3x^2 + 2xy^3) = 6x + 2y^3 , & f_{xy} &= \frac{\partial}{\partial y}(3x^2 + 2xy^3) = 6xy^2 , \\
> f_{yx} &= \frac{\partial}{\partial x}(3x^2 y^2 - 4y) = 6xy^2 , & f_{yy} &= \frac{\partial}{\partial y}(3x^2 y^2 - 4y) = 6x^2 y - 4 .
> \end{aligned}
> $$
>
> The two mixed partials agree, $f_{xy} = f_{yx}$; Clairaut's Theorem (Theorem §92.2) explains why.
>
> *Stewart: Examples 14.3.1 and 14.3.7*

^ex-92-1

> [!example] Example §92.2: Using the One-Variable Rules
> **(a)** If $f(x, y) = \sin\left( \dfrac{x}{1 + y} \right)$, calculate $\dfrac{\partial f}{\partial x}$ and $\dfrac{\partial f}{\partial y}$.
>
> By the Chain Rule for functions of one variable ([[§17 The Chain Rule#^thm-17-2|Theorem §17.2]]),
>
> $$
> \frac{\partial f}{\partial x} = \cos\left( \frac{x}{1 + y} \right) \cdot \frac{\partial}{\partial x}\left( \frac{x}{1 + y} \right) = \cos\left( \frac{x}{1 + y} \right) \cdot \frac{1}{1 + y} ,
> $$
>
> $$
> \frac{\partial f}{\partial y} = \cos\left( \frac{x}{1 + y} \right) \cdot \frac{\partial}{\partial y}\left( \frac{x}{1 + y} \right) = -\cos\left( \frac{x}{1 + y} \right) \cdot \frac{x}{(1 + y)^2} .
> $$
>
> **(b)** Find $f_x$, $f_y$ and $f_z$ if $f(x, y, z) = e^{xy} \ln z$ ([[§92 Partial Derivatives#^def-92-3|Definition §92.3]]).
>
> Holding $y$ and $z$ constant, $f_x = y e^{xy} \ln z$. Similarly $f_y = x e^{xy} \ln z$, and, holding $x$ and $y$ constant, $f_z = \dfrac{e^{xy}}{z}$.
>
> *Stewart: Examples 14.3.2 and 14.3.6*

^ex-92-2

## Interpretations of Partial Derivatives

> [!remark] Remark: Partial Derivatives as Slopes and as Rates of Change
> **Slopes.** The equation $z = f(x, y)$ represents a surface $S$, the graph of $f$. If $f(a, b) = c$, the point $P(a, b, c)$ lies on $S$. Fixing $y = b$ restricts attention to the curve $C_1$ in which the vertical plane $y = b$ intersects $S$ (the trace of $S$ in that plane). $C_1$ is the graph of $g(x) = f(x, b)$, so the slope of its tangent line $T_1$ at $P$ is $g'(a) = f_x(a, b)$. Likewise the plane $x = a$ cuts $S$ in a curve $C_2$, the graph of $G(y) = f(a, y)$, whose tangent $T_2$ at $P$ has slope $G'(b) = f_y(a, b)$. So $f_x(a, b)$ and $f_y(a, b)$ are the slopes of the tangent lines at $P$ to the traces of $S$ in the planes $y = b$ and $x = a$.
>
> **Rates of change.** If $z = f(x, y)$, then $\partial z / \partial x$ is the rate of change of $z$ with respect to $x$ when $y$ is fixed, and $\partial z / \partial y$ the rate of change with respect to $y$ when $x$ is fixed. For example, for the body mass index $B(m, h) = m/h^2$ of a man with $m = 64$ kg and $h = 1.68$ m, $\frac{\partial B}{\partial m} = \frac{1}{h^2} \approx 0.35$ (kg/m²)/kg and $\frac{\partial B}{\partial h} = -\frac{2m}{h^3} \approx -27$ (kg/m²)/m: one more kilogram raises his BMI by about $0.35$, while growing $1$ cm at constant weight lowers it by about $27(0.01) = 0.27$ (Stewart, Example 14.3.4).

^rem-92-1

> [!example] Example §92.3: Partial Derivatives as Slopes
> If $f(x, y) = 4 - x^2 - 2y^2$, find $f_x(1, 1)$ and $f_y(1, 1)$ and interpret these numbers as slopes.
>
> $$
> f_x(x, y) = -2x , \quad f_y(x, y) = -4y , \qquad f_x(1, 1) = -2 , \quad f_y(1, 1) = -4 .
> $$
>
> The graph of $f$ is the paraboloid $z = 4 - x^2 - 2y^2$, and $f(1, 1) = 1$. The vertical plane $y = 1$ intersects it in the parabola $C_1$: $z = 2 - x^2$, $y = 1$. The slope of its tangent line at $(1, 1, 1)$ is $f_x(1, 1) = -2$: the tangent line slopes downward in the positive $x$-direction. The plane $x = 1$ intersects the paraboloid in the parabola $C_2$: $z = 3 - 2y^2$, $x = 1$, and the slope of its tangent line at $(1, 1, 1)$ is $f_y(1, 1) = -4$. (Check: $\frac{d}{dx}(2 - x^2) = -2x = -2$ and $\frac{d}{dy}(3 - 2y^2) = -4y = -4$ at $x = 1$, $y = 1$.)
>
> *Stewart: Example 14.3.3*

^ex-92-3

![[m233-92-1.svg]]
*Example §92.3: the part of the paraboloid $z = 4 - x^2 - 2y^2$ over the first quadrant. The plane $y = 1$ cuts it in the parabola $C_1$ (blue), whose tangent $T_1$ at $P(1, 1, 1)$ (red) has slope $f_x(1, 1) = -2$ in the $x$-direction. The plane $x = 1$ cuts it in $C_2$ (green), whose tangent $T_2$ (orange) has slope $f_y(1, 1) = -4$ in the $y$-direction.*

> [!example] Example §92.4: Implicit Partial Differentiation
> Find $\partial z / \partial x$ and $\partial z / \partial y$ if $z$ is defined implicitly as a function of $x$ and $y$ by the equation
>
> $$
> x^3 + y^3 + z^3 + 6xyz + 4 = 0 .
> $$
>
> Then evaluate these partial derivatives at the point $(-1, 1, 2)$.
>
> **$\partial z / \partial x$.** Differentiate implicitly with respect to $x$, treating $y$ as a constant and $z$ as a function of $x$ (so the Product Rule applies to $6xyz$):
>
> $$
> 3x^2 + 3z^2 \frac{\partial z}{\partial x} + 6yz + 6xy \frac{\partial z}{\partial x} = 0
> \quad\Longrightarrow\quad
> \frac{\partial z}{\partial x} = -\frac{x^2 + 2yz}{z^2 + 2xy} .
> $$
>
> **$\partial z / \partial y$.** In the same way, differentiating with respect to $y$ with $x$ constant,
>
> $$
> 3y^2 + 3z^2 \frac{\partial z}{\partial y} + 6xz + 6xy \frac{\partial z}{\partial y} = 0
> \quad\Longrightarrow\quad
> \frac{\partial z}{\partial y} = -\frac{y^2 + 2xz}{z^2 + 2xy} .
> $$
>
> **At $(-1, 1, 2)$.** The point lies on the surface: $(-1)^3 + 1^3 + 2^3 + 6(-1)(1)(2) + 4 = -1 + 1 + 8 - 12 + 4 = 0$. There
>
> $$
> \frac{\partial z}{\partial x} = -\frac{(-1)^2 + 2 \cdot 1 \cdot 2}{2^2 + 2(-1) \cdot 1} = -\frac52 ,
> \qquad
> \frac{\partial z}{\partial y} = -\frac{1^2 + 2(-1) \cdot 2}{2^2 + 2(-1) \cdot 1} = \frac32 .
> $$
>
> A shortcut through the Chain Rule is [[§94 The Chain Rule#^thm-94-5|Theorem §94.5]].
>
> *Stewart: Example 14.3.5*

^ex-92-4

## Functions of More Than Two Variables

> [!definition] Definition §92.3: Partial Derivatives of Functions of Three or More Variables
> If $f$ is a function of three variables $x$, $y$, $z$, its partial derivative with respect to $x$ is
>
> $$
> f_x(x, y, z) = \lim_{h \to 0} \frac{f(x + h, y, z) - f(x, y, z)}{h} ,
> $$
>
> found by regarding $y$ and $z$ as constants and differentiating with respect to $x$. In general, if $u = f(x_1, x_2, \ldots, x_n)$, its partial derivative with respect to the $i$th variable $x_i$ is
>
> $$
> \frac{\partial u}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1, \ldots, x_{i-1}, x_i + h, x_{i+1}, \ldots, x_n) - f(x_1, \ldots, x_i, \ldots, x_n)}{h} ,
> $$
>
> also written $\dfrac{\partial u}{\partial x_i} = \dfrac{\partial f}{\partial x_i} = f_{x_i} = f_i = D_i f$.
>
> *Stewart: 14.3 (text)*

^def-92-3

If $w = f(x, y, z)$, then $f_x = \partial w / \partial x$ is the rate of change of $w$ with respect to $x$ when $y$ and $z$ are held fixed. It has no slope interpretation, since the graph of $f$ lies in four-dimensional space.

## Higher Derivatives

> [!definition] Definition §92.4: Second Partial Derivatives
> If $f$ is a function of two variables, its partial derivatives $f_x$ and $f_y$ are again functions of two variables, and their partial derivatives $(f_x)_x$, $(f_x)_y$, $(f_y)_x$, $(f_y)_y$ are the **second partial derivatives** of $f$. If $z = f(x, y)$:
>
> $$
> \begin{aligned}
> (f_x)_x &= f_{xx} = f_{11} = \frac{\partial}{\partial x}\left( \frac{\partial f}{\partial x} \right) = \frac{\partial^2 f}{\partial x^2} = \frac{\partial^2 z}{\partial x^2} , \\
> (f_x)_y &= f_{xy} = f_{12} = \frac{\partial}{\partial y}\left( \frac{\partial f}{\partial x} \right) = \frac{\partial^2 f}{\partial y\,\partial x} = \frac{\partial^2 z}{\partial y\,\partial x} , \\
> (f_y)_x &= f_{yx} = f_{21} = \frac{\partial}{\partial x}\left( \frac{\partial f}{\partial y} \right) = \frac{\partial^2 f}{\partial x\,\partial y} = \frac{\partial^2 z}{\partial x\,\partial y} , \\
> (f_y)_y &= f_{yy} = f_{22} = \frac{\partial}{\partial y}\left( \frac{\partial f}{\partial y} \right) = \frac{\partial^2 f}{\partial y^2} = \frac{\partial^2 z}{\partial y^2} .
> \end{aligned}
> $$
>
> So $f_{xy}$ (or $\partial^2 f / \partial y\,\partial x$) means that we first differentiate with respect to $x$ and then with respect to $y$; in $f_{yx}$ the order is reversed. Partial derivatives of order $3$ or higher are defined in the same way, for instance $f_{xyy} = (f_{xy})_y = \dfrac{\partial}{\partial y}\left( \dfrac{\partial^2 f}{\partial y\,\partial x} \right) = \dfrac{\partial^3 f}{\partial y^2\,\partial x}$.
>
> *Stewart: 14.3 (text)*

^def-92-4

> [!theorem] Theorem §92.2: Clairaut's Theorem
> Suppose $f$ is defined on a disk $D$ that contains the point $(a, b)$. If the functions $f_{xy}$ and $f_{yx}$ are both continuous on $D$, then
>
> $$
> f_{xy}(a, b) = f_{yx}(a, b) .
> $$
>
> *Stewart: 14.3, Clairaut's Theorem; proof in Appendix F*

^thm-92-2

> [!remark] Remark: Why It Works
> Both mixed partials are limits of the same "second difference"
>
> $$
> \Delta(h) = f(a + h, b + h) - f(a + h, b) - f(a, b + h) + f(a, b) ,
> $$
>
> the alternating sum of $f$ over the four corners of a small square. Grouping the four terms in pairs along the $y$-direction first and then along $x$ gives approximately $h^2 f_{xy}$; grouping them the other way round gives approximately $h^2 f_{yx}$. The Mean Value Theorem makes "approximately" precise, and continuity lets $h \to 0$.

^rem-92-2

> [!proof]+ Proof
> Take $h \ne 0$ so small that the closed square with corners $(a, b)$ and $(a + h, b + h)$ lies in $D$. (The existence of $f_{xy}$ and $f_{yx}$ on $D$ includes the existence of $f_x$ and $f_y$ there.) Consider
>
> $$
> \Delta(h) = \big[ f(a + h, b + h) - f(a + h, b) \big] - \big[ f(a, b + h) - f(a, b) \big] .
> $$
>
> **Via $f_{xy}$.** Let $g(x) = f(x, b + h) - f(x, b)$. Then $\Delta(h) = g(a + h) - g(a)$. The function $g$ is differentiable between $a$ and $a + h$, with $g'(x) = f_x(x, b + h) - f_x(x, b)$, so by the Mean Value Theorem ([[§26 The Mean Value Theorem#^thm-26-2|Theorem §26.2]]) there is a number $c$ between $a$ and $a + h$ such that
>
> $$
> g(a + h) - g(a) = g'(c)\,h = h \big[ f_x(c, b + h) - f_x(c, b) \big] .
> $$
>
> Applying the Mean Value Theorem again, this time to the function $y \mapsto f_x(c, y)$, whose derivative is $f_{xy}(c, y)$, we get a number $d$ between $b$ and $b + h$ such that
>
> $$
> f_x(c, b + h) - f_x(c, b) = f_{xy}(c, d)\,h .
> $$
>
> Combining, $\Delta(h) = h^2 f_{xy}(c, d)$. If $h \to 0$, then $(c, d) \to (a, b)$, since $|c - a| \le |h|$ and $|d - b| \le |h|$. So the continuity of $f_{xy}$ at $(a, b)$ gives
>
> $$
> \lim_{h \to 0} \frac{\Delta(h)}{h^2} = \lim_{(c, d) \to (a, b)} f_{xy}(c, d) = f_{xy}(a, b) .
> $$
>
> **Via $f_{yx}$.** Regroup the same four terms:
>
> $$
> \Delta(h) = \big[ f(a + h, b + h) - f(a, b + h) \big] - \big[ f(a + h, b) - f(a, b) \big] .
> $$
>
> With $G(y) = f(a + h, y) - f(a, y)$ we have $\Delta(h) = G(b + h) - G(b)$. (Stewart writes "similarly"; the steps are these.) The Mean Value Theorem gives $d'$ between $b$ and $b + h$ with $\Delta(h) = h\,G'(d') = h \big[ f_y(a + h, d') - f_y(a, d') \big]$, and then, applied to $x \mapsto f_y(x, d')$, a number $c'$ between $a$ and $a + h$ with $f_y(a + h, d') - f_y(a, d') = f_{yx}(c', d')\,h$. So $\Delta(h) = h^2 f_{yx}(c', d')$, and the continuity of $f_{yx}$ at $(a, b)$ gives $\lim_{h \to 0} \Delta(h)/h^2 = f_{yx}(a, b)$.
>
> The two limits are limits of the same quantity, so $f_{xy}(a, b) = f_{yx}(a, b)$.

^pf-92-2

*Uses:* [[§92 Partial Derivatives#^def-92-4|Def. §92.4]], [[§26 The Mean Value Theorem#^thm-26-2|§26.2]] (Mean Value Theorem), [[§91 Limits and Continuity#^def-91-3|Def. §91.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§5 Equality of Mixed Partials#^thm-5-1|452 Thm. §5.1]] (on an open rectangle, by the same second-difference argument); hub [[Schwarz–Clairaut Theorem]].

Using Clairaut's Theorem repeatedly, one shows that $f_{xyy} = f_{yxy} = f_{yyx}$ if these functions are continuous: third and higher partial derivatives also do not depend on the order of differentiation.

> [!example] Example §92.5: Higher-Order Partial Derivatives
> **(a)** Calculate $f_{xxyz}$ if $f(x, y, z) = \sin(3x + yz)$.
>
> Differentiate in the order of the subscripts, $x$, $x$, $y$, $z$, using the Chain Rule (and, in the last step, the Product Rule):
>
> $$
> \begin{aligned}
> f_x &= 3\cos(3x + yz) , & f_{xx} &= -9\sin(3x + yz) , \\
> f_{xxy} &= -9z\cos(3x + yz) , & f_{xxyz} &= -9\cos(3x + yz) + 9yz\sin(3x + yz) .
> \end{aligned}
> $$
>
> **(b)** If $V = \ln(u + v^2 + w^4)$, compute $\dfrac{\partial^3 V}{\partial u\,\partial v\,\partial w}$.
>
> Write $S = u + v^2 + w^4$. By Clairaut's Theorem the order does not matter (all partial derivatives of $V$ are continuous where $S > 0$), so differentiate in the easiest order, $u$, then $v$, then $w$:
>
> $$
> V_u = S^{-1} , \qquad V_{uv} = -S^{-2} \cdot 2v = -2v\,S^{-2} , \qquad V_{uvw} = -2v \cdot (-2) S^{-3} \cdot 4w^3 = \frac{16\,v\,w^3}{(u + v^2 + w^4)^3} .
> $$
>
> **(c)** If $f(x, y) = \displaystyle\int_y^x \tan(1 + t^2)\,dt$, compute $f_x$, $f_y$, $f_{xx}$, $f_{yy}$, $f_{xy}$, $f_{yx}$.
>
> By the Fundamental Theorem of Calculus, Part 1 ([[§36 The Fundamental Theorem of Calculus#^thm-36-1|Theorem §36.1]]), with the other limit held fixed, and $\int_y^x = -\int_x^y$:
>
> $$
> f_x = \tan(1 + x^2) , \qquad f_y = -\tan(1 + y^2) .
> $$
>
> (The integrand is continuous where $\cos(1 + t^2) \ne 0$, so these hold for $x$ and $y$ in an interval avoiding such points.) Then $f_x$ depends only on $x$ and $f_y$ only on $y$, so
>
> $$
> f_{xx} = 2x \sec^2(1 + x^2) , \qquad f_{yy} = -2y \sec^2(1 + y^2) , \qquad f_{xy} = f_{yx} = 0 .
> $$
>
> *Stewart: Example 14.3.8*
> *Source: 233 Midterm 1 Practice Questions, Q24*

^ex-92-5

## Partial Differential Equations

> [!definition] Definition §92.5: Laplace's Equation and the Wave Equation
> The partial differential equation
>
> $$
> \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0
> $$
>
> is **Laplace's equation**, and its solutions are called **harmonic functions**. The three-dimensional Laplace equation is
>
> $$
> \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} = 0 . \qquad (5)
> $$
>
> The **wave equation** is
>
> $$
> \frac{\partial^2 u}{\partial t^2} = a^2 \frac{\partial^2 u}{\partial x^2} ,
> $$
>
> where $a$ is a constant. For instance, $u(x, y) = e^x \sin y$ is harmonic: $u_{xx} = e^x \sin y$ and $u_{yy} = -e^x \sin y$, so $u_{xx} + u_{yy} = 0$. And $u(x, t) = \sin(x - at)$ satisfies the wave equation: $u_{xx} = -\sin(x - at)$ and $u_{tt} = -a^2 \sin(x - at) = a^2 u_{xx}$.
>
> *Stewart: 14.3, Equation 5, text and Examples 14.3.9, 14.3.10*

^def-92-5

> [!remark]- Connections
> - PDE version: [[§35 Potential Equation#^def-35-1|341 Def. §35.1]] (Laplace's equation and harmonic functions, solved in rectangles and disks), [[§29 The Vibrating String#^def-29-2|341 Def. §29.2]] (the wave equation of a vibrating string) and [[§31 d'Alembert's Solution#^thm-31-2|341 Thm. §31.2]] (every solution of the wave equation has the form $\psi(x + ct) + \phi(x - ct)$, like $\sin(x - at)$ here).

Harmonic functions describe heat conduction, fluid flow and electric potential; the three-dimensional equation (5) governs, for instance, the strength $u(x, y, z)$ of a magnetic field in geophysics. In the wave equation, $u(x, t)$ is the displacement at time $t$ and at distance $x$ from one end of a vibrating violin string, and $a$ depends on the density and the tension of the string.
