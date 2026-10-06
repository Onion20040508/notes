---
type: section
subject: "[[Calculus]]"
chapter: 14
section: 93
stewart: "14.4"
aliases: ["Stewart 14.4"]
tags: [calculus, math233]
---
← [[§92 Partial Derivatives]] · ↑ [[· 14 Partial Derivatives]] · [[§94 The Chain Rule]] →

*Stewart, Section 14.4 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q27), Practice Exam 1 (Q1(e), Q4(a)).*

As we zoom in toward a point on the graph of a differentiable function of one variable, the graph becomes indistinguishable from its tangent line ([[§23 Linear Approximations and Differentials#^def-23-1|Definition §23.1]]). One dimension up, a surface $z = f(x, y)$ that is the graph of a differentiable function looks more and more like a plane, its tangent plane, and $f$ is approximated near the point by a linear function of two variables. The tangent plane is built from the two partial derivatives. But partial derivatives alone do not guarantee that the approximation is good, so this section defines *differentiability* for functions of two variables and gives the practical test for it: continuous partial derivatives. Differentials then package the linear approximation for estimating changes and errors.

## Tangent Planes

> [!definition] Definition §93.1: Tangent Plane
> Suppose a surface $S$ has equation $z = f(x, y)$, where $f$ has continuous first partial derivatives, and let $P(x_0, y_0, z_0)$ be a point on $S$. Let $C_1$ and $C_2$ be the curves in which the vertical planes $y = y_0$ and $x = x_0$ intersect $S$, and let $T_1$ and $T_2$ be the tangent lines to $C_1$ and $C_2$ at $P$ ([[§92 Partial Derivatives#^rem-92-1|§92, Remark]]). The **tangent plane** to the surface $S$ at the point $P$ is the plane that contains both tangent lines $T_1$ and $T_2$.
>
> *Stewart: 14.4 (text)*

^def-93-1

We will see in [[§95 Directional Derivatives and the Gradient Vector#^thm-95-5|Theorem §95.5]] that the tangent line at $P$ to *any* curve $C$ that lies on $S$ and passes through $P$ also lies in the tangent plane. So the tangent plane consists of all possible tangent lines at $P$ to curves on $S$ through $P$: it is the plane that most closely approximates $S$ near $P$.

> [!theorem] Theorem §93.1: Equation of a Tangent Plane
> Suppose $f$ has continuous partial derivatives. An equation of the tangent plane to the surface $z = f(x, y)$ at the point $P(x_0, y_0, z_0)$ is
>
> $$
> z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) .
> $$
>
> *Stewart: 14.4, Equation 2*

^thm-93-1

> [!proof]+ Proof
> Any plane through $P(x_0, y_0, z_0)$ has an equation $A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$ ([[§84 Equations of Lines and Planes#^prop-84-6|Proposition §84.6]], Stewart's Equation 12.5.7). The tangent plane is not vertical, that is, $C \ne 0$: it contains the lines $T_1$ and $T_2$, with direction vectors $\langle 1, 0, m_1 \rangle$ and $\langle 0, 1, m_2 \rangle$ ($m_1$, $m_2$ their slopes), so it has the normal vector $\langle 1, 0, m_1 \rangle \times \langle 0, 1, m_2 \rangle = \langle -m_1, -m_2, 1 \rangle$, whose third component is not $0$. (Stewart divides by $C$ without comment; this is why it is allowed.) Dividing by $C$ and letting $a = -A/C$, $b = -B/C$, the equation becomes
>
> $$
> z - z_0 = a(x - x_0) + b(y - y_0) . \qquad (1)
> $$
>
> The intersection of this plane with the plane $y = y_0$ must be the tangent line $T_1$. Setting $y = y_0$ in (1) gives
>
> $$
> z - z_0 = a(x - x_0) , \qquad y = y_0 ,
> $$
>
> the point-slope equation of a line with slope $a$. But the slope of $T_1$ is $f_x(x_0, y_0)$ ([[§92 Partial Derivatives#^rem-92-1|§92, Remark]]). Therefore $a = f_x(x_0, y_0)$. Similarly, putting $x = x_0$ in (1) gives $z - z_0 = b(y - y_0)$, which must represent $T_2$, so $b = f_y(x_0, y_0)$.

^pf-93-1

*Uses:* [[§93 Tangent Planes and Linear Approximations#^def-93-1|Def. §93.1]], [[§92 Partial Derivatives#^rem-92-1|§92]] (partial derivatives as slopes), [[§84 Equations of Lines and Planes#^prop-84-6|§84.6]] (equation of a plane), [[§83 The Cross Product#^thm-83-2|§83.2]] (normal vector)

Compare the tangent line $y - y_0 = f'(x_0)(x - x_0)$ in one variable.

> [!example] Example §93.1: Tangent Plane and Linear Approximation
> Find the tangent plane to the elliptic paraboloid $z = 2x^2 + y^2$ at the point $(1, 1, 3)$, and use it to approximate $f(x, y) = 2x^2 + y^2$ near $(1, 1)$.
>
> $$
> f_x(x, y) = 4x , \quad f_y(x, y) = 2y , \qquad f_x(1, 1) = 4 , \quad f_y(1, 1) = 2 .
> $$
>
> By Theorem §93.1 the tangent plane at $(1, 1, 3)$ is
>
> $$
> z - 3 = 4(x - 1) + 2(y - 1) , \qquad\text{or}\qquad z = 4x + 2y - 3 .
> $$
>
> **Approximation.** The linear function $L(x, y) = 4x + 2y - 3$, whose graph is this plane, is a good approximation to $f(x, y)$ for $(x, y)$ near $(1, 1)$:
>
> $$
> f(1.1, 0.95) \approx 4(1.1) + 2(0.95) - 3 = 3.3 , \qquad\text{true value } 2(1.1)^2 + (0.95)^2 = 3.3225 .
> $$
>
> Farther away it is poor: $L(2, 3) = 11$, whereas $f(2, 3) = 17$. Zooming in toward $(1, 1, 3)$, the paraboloid looks flatter and flatter and more and more like its tangent plane; on a contour map, the level curves near $(1, 1)$ look more and more like equally spaced parallel lines, the contour map of a plane.
>
> *Stewart: Example 14.4.1 and text*

^ex-93-1

## Linear Approximations

> [!definition] Definition §93.2: Linearization and Linear Approximation
> The linear function
>
> $$
> L(x, y) = f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b) \qquad (3)
> $$
>
> whose graph is the tangent plane at $(a, b, f(a, b))$ is the **linearization** of $f$ at $(a, b)$, and the approximation
>
> $$
> f(x, y) \approx f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b) \qquad (4)
> $$
>
> is the **linear approximation** or **tangent plane approximation** of $f$ at $(a, b)$.
>
> *Stewart: 14.4, Equations 3 and 4*

^def-93-2

> [!remark] Remark: Partial Derivatives Are Not Enough
> The tangent plane was defined for $f$ with *continuous* first partial derivatives. Without continuity, things can go wrong. Let
>
> $$
> f(x, y) = \frac{xy}{x^2 + y^2} \ \text{ if } (x, y) \ne (0, 0) , \qquad f(0, 0) = 0 .
> $$
>
> Since $f(h, 0) = 0 = f(0, h)$ for all $h$, Equations (2) and (3) of [[§92 Partial Derivatives#^def-92-1|Definition §92.1]] give $f_x(0, 0) = 0$ and $f_y(0, 0) = 0$; but $f_x$ and $f_y$ are not continuous at the origin (Stewart, Exercise 54). The "linear approximation" at the origin would be $f(x, y) \approx 0$, yet $f(x, y) = \frac12$ at every point of the line $y = x$ except the origin ([[§91 Limits and Continuity#^ex-91-1|Example §91.1]](b)). So a function of two variables can behave badly even though both of its partial derivatives exist. Differentiability rules this out.

^rem-93-1

For one variable, if $y = f(x)$ is differentiable at $a$ and $x$ changes from $a$ to $a + \Delta x$, the increment $\Delta y = f(a + \Delta x) - f(a)$ satisfies
$$
\Delta y = f'(a)\,\Delta x + \varepsilon\,\Delta x \quad\text{where } \varepsilon \to 0 \text{ as } \Delta x \to 0 \qquad (5)
$$
(Stewart, Equation 3.4.7; [[§17 The Chain Rule#^lem-17-1|Lemma §17.1]]). The definition for two variables copies this.

> [!definition] Definition §93.3: Increment; Differentiable Function of Two Variables
> Let $z = f(x, y)$. If $x$ changes from $a$ to $a + \Delta x$ and $y$ changes from $b$ to $b + \Delta y$, the corresponding **increment** of $z$ is
>
> $$
> \Delta z = f(a + \Delta x, b + \Delta y) - f(a, b) . \qquad (6)
> $$
>
> The function $f$ is **differentiable** at $(a, b)$ if $\Delta z$ can be expressed in the form
>
> $$
> \Delta z = f_x(a, b)\,\Delta x + f_y(a, b)\,\Delta y + \varepsilon_1\,\Delta x + \varepsilon_2\,\Delta y ,
> $$
>
> where $\varepsilon_1$ and $\varepsilon_2$ are functions of $\Delta x$ and $\Delta y$ such that $\varepsilon_1 \to 0$ and $\varepsilon_2 \to 0$ as $(\Delta x, \Delta y) \to (0, 0)$.
>
> *Stewart: 14.4, Equation 6 and Definition 7*

^def-93-3

In words: $f$ is differentiable at $(a, b)$ when the linear approximation (4) is a good approximation for $(x, y)$ near $(a, b)$, that is, when the tangent plane approximates the graph of $f$ well near the point of tangency. It is often hard to check Definition §93.3 directly; the next theorem is the convenient sufficient condition.

> [!remark]- Connections
> - Rigorous treatment: [[§6 Differentiability#^def-6-1|452 Def. §6.1]] asks for $\Delta z = A\,\Delta x + B\,\Delta y + o\big(\sqrt{\Delta x^2 + \Delta y^2}\big)$. This is equivalent to Stewart's form, with $\rho = \sqrt{\Delta x^2 + \Delta y^2}$: $\varepsilon_1 \Delta x + \varepsilon_2 \Delta y$ is $o(\rho)$ since $|\Delta x|, |\Delta y| \le \rho$; conversely an $o(\rho)$ remainder $R$ equals $\varepsilon_1 \Delta x + \varepsilon_2 \Delta y$ with $\varepsilon_1 = R\,\Delta x / \rho^2$ and $\varepsilon_2 = R\,\Delta y / \rho^2$, both at most $|R|/\rho$ in absolute value. The function of the remark "Partial Derivatives Are Not Enough", doubled, is [[§6 Differentiability#^ex-6-1|452 Ex. §6.1]], and the derivative as a linear map is [[§6 Differentiability#^def-6-2|452 Def. §6.2]].

> [!theorem] Theorem §93.2: Continuous Partial Derivatives Imply Differentiability
> If the partial derivatives $f_x$ and $f_y$ exist near $(a, b)$ and are continuous at $(a, b)$, then $f$ is differentiable at $(a, b)$.
>
> *Stewart: 14.4, Theorem 8; proof in Appendix F*

^thm-93-2

> [!proof]+ Proof
> Let $\Delta z = f(a + \Delta x, b + \Delta y) - f(a, b)$. By Definition §93.3 we have to show that
>
> $$
> \Delta z = f_x(a, b)\,\Delta x + f_y(a, b)\,\Delta y + \varepsilon_1\,\Delta x + \varepsilon_2\,\Delta y
> $$
>
> where $\varepsilon_1, \varepsilon_2 \to 0$ as $(\Delta x, \Delta y) \to (0, 0)$. Take $(\Delta x, \Delta y)$ so small that the rectangle $R$ with opposite corners $(a, b)$ and $(a + \Delta x, b + \Delta y)$ lies in a disk around $(a, b)$ on which $f_x$ and $f_y$ exist. Go from $(a, b)$ to $(a + \Delta x, b + \Delta y)$ in two steps, first up and then across:
>
> $$
> \Delta z = \big[ f(a + \Delta x, b + \Delta y) - f(a, b + \Delta y) \big] + \big[ f(a, b + \Delta y) - f(a, b) \big] . \qquad (1)
> $$
>
> **First bracket.** The function of one variable $g(x) = f(x, b + \Delta y)$ is defined on the interval between $a$ and $a + \Delta x$, with $g'(x) = f_x(x, b + \Delta y)$. By the Mean Value Theorem ([[§26 The Mean Value Theorem#^thm-26-2|Theorem §26.2]]; $g$ is differentiable, hence continuous) there is a number $u$ between $a$ and $a + \Delta x$ with $g(a + \Delta x) - g(a) = g'(u)\,\Delta x$, that is,
>
> $$
> f(a + \Delta x, b + \Delta y) - f(a, b + \Delta y) = f_x(u, b + \Delta y)\,\Delta x .
> $$
>
> **Second bracket.** Let $h(y) = f(a, y)$, defined on the interval between $b$ and $b + \Delta y$, with $h'(y) = f_y(a, y)$. A second application of the Mean Value Theorem gives a number $v$ between $b$ and $b + \Delta y$ with
>
> $$
> f(a, b + \Delta y) - f(a, b) = f_y(a, v)\,\Delta y .
> $$
>
> (If $\Delta x = 0$ or $\Delta y = 0$, take $u = a$ or $v = b$.) Substituting into (1),
>
> $$
> \begin{aligned}
> \Delta z &= f_x(u, b + \Delta y)\,\Delta x + f_y(a, v)\,\Delta y \\
> &= f_x(a, b)\,\Delta x + \big[ f_x(u, b + \Delta y) - f_x(a, b) \big] \Delta x + f_y(a, b)\,\Delta y + \big[ f_y(a, v) - f_y(a, b) \big] \Delta y \\
> &= f_x(a, b)\,\Delta x + f_y(a, b)\,\Delta y + \varepsilon_1\,\Delta x + \varepsilon_2\,\Delta y ,
> \end{aligned}
> $$
>
> where
>
> $$
> \varepsilon_1 = f_x(u, b + \Delta y) - f_x(a, b) , \qquad \varepsilon_2 = f_y(a, v) - f_y(a, b) .
> $$
>
> As $(\Delta x, \Delta y) \to (0, 0)$, the points $(u, b + \Delta y)$ and $(a, v)$ tend to $(a, b)$, since $|u - a| \le |\Delta x|$ and $|v - b| \le |\Delta y|$. Since $f_x$ and $f_y$ are continuous at $(a, b)$, $\varepsilon_1 \to 0$ and $\varepsilon_2 \to 0$. Therefore $f$ is differentiable at $(a, b)$.

^pf-93-2

*Uses:* [[§93 Tangent Planes and Linear Approximations#^def-93-3|Def. §93.3]], [[§26 The Mean Value Theorem#^thm-26-2|§26.2]] (Mean Value Theorem), [[§91 Limits and Continuity#^def-91-3|Def. §91.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§6 Differentiability#^thm-6-2|452 Thm. §6.2]], with the same two-step Mean Value Theorem argument; hub [[Continuous Partials Imply Differentiability]].

> [!example] Example §93.2: Differentiability and Linearization
> **(a)** Show that $f(x, y) = xe^{xy}$ is differentiable at $(1, 0)$ and find its linearization there. Then use it to approximate $f(1.1, -0.1)$.
>
> $$
> f_x(x, y) = e^{xy} + xye^{xy} , \quad f_y(x, y) = x^2 e^{xy} , \qquad f_x(1, 0) = 1 , \quad f_y(1, 0) = 1 .
> $$
>
> Both $f_x$ and $f_y$ are continuous functions (sums and products of polynomials and exponentials, [[§91 Limits and Continuity#^thm-91-5|Theorem §91.5]]), so $f$ is differentiable by Theorem §93.2. With $f(1, 0) = 1$, the linearization is
>
> $$
> L(x, y) = f(1, 0) + f_x(1, 0)(x - 1) + f_y(1, 0)(y - 0) = 1 + (x - 1) + y = x + y .
> $$
>
> So $xe^{xy} \approx x + y$ near $(1, 0)$, and $f(1.1, -0.1) \approx 1.1 - 0.1 = 1$. Compare the actual value $f(1.1, -0.1) = 1.1\,e^{-0.11} \approx 0.98542$.
>
> **(b)** Find a linear approximation of the heat index $I = f(T, H)$ when $T$ is near $96$°F and $H$ is near $70$%, and use it to estimate the heat index when $T = 97$°F and $H = 72$%.
>
> Here $f$ is known only through the National Weather Service table at the start of [[§92 Partial Derivatives|§92]]. It gives $f(96, 70) = 125$, and its difference quotients gave $f_T(96, 70) \approx 3.75$ and $f_H(96, 70) \approx 0.9$. So
>
> $$
> f(T, H) \approx 125 + 3.75(T - 96) + 0.9(H - 70) , \qquad f(97, 72) \approx 125 + 3.75(1) + 0.9(2) = 130.55 ,
> $$
>
> and the heat index is $I \approx 131$°F.
>
> **(c)** Find the linear approximation $L(x, y)$ of $f(x, y) = xye^x$ at $(1, 1)$ and use it to estimate $f(1.1, 0.9)$. (Choices: $1.1e$, $e$, $0.5$, $1.5$, $2e$, $2$.)
>
> $f(1, 1) = e$, $f_x = ye^x + xye^x$, so $f_x(1, 1) = 2e$, and $f_y = xe^x$, so $f_y(1, 1) = e$. Hence $L(x, y) = e + 2e(x - 1) + e(y - 1)$ and
>
> $$
> f(1.1, 0.9) \approx e + 2e(0.1) + e(-0.1) = 1.1e . \qquad \textbf{Answer: } 1.1e .
> $$
>
> **(d)** Let $f(x, y) = x^2 y + y e^{xy}$. Find the linearization $L(x, y)$ of $f$ at $(0, 5)$ and use it to approximate $f(0.1, 4.9)$.
>
> $f(0, 5) = 0 + 5e^0 = 5$, and
>
> $$
> f_x = 2xy + y^2 e^{xy} , \quad f_y = x^2 + e^{xy} + xye^{xy} , \qquad f_x(0, 5) = 0 + 25 = 25 , \quad f_y(0, 5) = 0 + 1 + 0 = 1 .
> $$
>
> Both partial derivatives are continuous, so $f$ is differentiable (Theorem §93.2), and
>
> $$
> L(x, y) = 5 + 25(x - 0) + 1(y - 5) = 25x + y , \qquad f(0.1, 4.9) \approx L(0.1, 4.9) = 2.5 + 4.9 = 7.4 .
> $$
>
> The actual value is $f(0.1, 4.9) = 0.049 + 4.9e^{0.49} \approx 8.047$. The estimate is rougher than in (a) because the graph bends sharply in the $x$-direction at $(0, 5)$: $f_{xx} = 2y + y^3 e^{xy}$ equals $135$ there.
>
> *In (d), the posted exam and its answer key write the point as "(0.5)"; the key's solution shows that $(0, 5)$ is meant.*
>
> *Stewart: Examples 14.4.2 and 14.4.3*
> *Source: 233 Practice Exam 1, Q1(e) and Q4(a)*

^ex-93-2

## Differentials

> [!definition] Definition §93.4: Differentials
> For a differentiable function of two variables, $z = f(x, y)$, the **differentials** $dx$ and $dy$ are independent variables: they can be given any values. The **differential** $dz$, also called the **total differential**, is then
>
> $$
> dz = f_x(x, y)\,dx + f_y(x, y)\,dy = \frac{\partial z}{\partial x}\,dx + \frac{\partial z}{\partial y}\,dy . \qquad (10)
> $$
>
> Sometimes $df$ is written for $dz$.
>
> *Stewart: 14.4, Equation 10*

^def-93-4

Compare $dy = f'(x)\,dx$ in one variable ([[§23 Linear Approximations and Differentials#^def-23-2|Definition §23.2]]). Taking $dx = \Delta x = x - a$ and $dy = \Delta y = y - b$ in (10), the differential of $z$ at $(a, b)$ is
$$
dz = f_x(a, b)(x - a) + f_y(a, b)(y - b) ,
$$
so the linear approximation (4) reads $f(x, y) \approx f(a, b) + dz$. Geometrically, $dz$ is the change in height of the **tangent plane**, whereas $\Delta z$ is the change in height of the **surface** $z = f(x, y)$, when $(x, y)$ changes from $(a, b)$ to $(a + \Delta x, b + \Delta y)$.

![[m233-93-1.svg]]
*The increment $\Delta z$ and the differential $dz$. Over the base rectangle from $(a, b)$ to $(a + \Delta x, b + \Delta y)$, the surface $z = f(x, y)$ (blue) rises by $\Delta z$, its tangent plane at $(a, b, f(a, b))$ (green) by $dz$. For a differentiable $f$ the difference $\Delta z - dz$ is small compared with the size of $(\Delta x, \Delta y)$.*

> [!remark]- Connections
> - Rigorous treatment: [[§8 The Differential#^def-8-1|452 Def. §8.1]] (the differential as the linear map $(dx, dy) \mapsto f_x\,dx + f_y\,dy$), with higher differentials in [[§8 The Differential#^def-8-2|452 Def. §8.2]].

> [!example] Example §93.3: Differential Versus Increment
> **(a)** If $z = f(x, y) = x^2 + 3xy - y^2$, find the differential $dz$.
>
> $$
> dz = \frac{\partial z}{\partial x}\,dx + \frac{\partial z}{\partial y}\,dy = (2x + 3y)\,dx + (3x - 2y)\,dy .
> $$
>
> **(b)** If $x$ changes from $2$ to $2.05$ and $y$ changes from $3$ to $2.96$, compare the values of $\Delta z$ and $dz$.
>
> Put $x = 2$, $dx = \Delta x = 0.05$, $y = 3$, $dy = \Delta y = -0.04$:
>
> $$
> dz = [2(2) + 3(3)](0.05) + [3(2) - 2(3)](-0.04) = 13(0.05) + 0 = 0.65 .
> $$
>
> The increment is
>
> $$
> \begin{aligned}
> \Delta z = f(2.05, 2.96) - f(2, 3) &= \big[ (2.05)^2 + 3(2.05)(2.96) - (2.96)^2 \big] - \big[ 2^2 + 3(2)(3) - 3^2 \big] \\
> &= [4.2025 + 18.204 - 8.7616] - 13 = 13.6449 - 13 = 0.6449 .
> \end{aligned}
> $$
>
> So $\Delta z \approx dz$, but $dz$ is easier to compute. The tangent plane is a good approximation to the surface near $(2, 3, 13)$.
>
> *Stewart: Example 14.4.4*

^ex-93-3

## Functions of Three or More Variables

> [!definition] Definition §93.5: Linear Approximation and Differentials in Three Variables
> Linear approximations, differentiability and differentials are defined in the same way for functions of more than two variables; a differentiable function is defined by an expression like the one in Definition §93.3. For $f(x, y, z)$ the **linear approximation** at $(a, b, c)$ is
>
> $$
> f(x, y, z) \approx f(a, b, c) + f_x(a, b, c)(x - a) + f_y(a, b, c)(y - b) + f_z(a, b, c)(z - c) ,
> $$
>
> and the **linearization** $L(x, y, z)$ is the right side. If $w = f(x, y, z)$, the **increment** of $w$ is $\Delta w = f(x + \Delta x, y + \Delta y, z + \Delta z) - f(x, y, z)$, and the **differential** $dw$ is defined in terms of the differentials $dx$, $dy$, $dz$ of the independent variables by
>
> $$
> dw = \frac{\partial w}{\partial x}\,dx + \frac{\partial w}{\partial y}\,dy + \frac{\partial w}{\partial z}\,dz .
> $$
>
> *Stewart: 14.4 (text)*

^def-93-5

> [!example] Example §93.4: Estimating Errors with Differentials
> **(a)** The base radius and height of a right circular cone are measured as $10$ cm and $25$ cm, with a possible error of as much as $\varepsilon$ cm in each. Estimate the maximum error in the calculated volume, and evaluate it for $\varepsilon = 0.1$.
>
> $V = \pi r^2 h / 3$, so
>
> $$
> dV = \frac{\partial V}{\partial r}\,dr + \frac{\partial V}{\partial h}\,dh = \frac{2\pi r h}{3}\,dr + \frac{\pi r^2}{3}\,dh .
> $$
>
> Each error is at most $\varepsilon$: $|\Delta r| \le \varepsilon$, $|\Delta h| \le \varepsilon$. The largest error in $V$ comes from the largest errors in $r$ and $h$, so take $dr = dh = \varepsilon$ with $r = 10$, $h = 25$:
>
> $$
> \Delta V \approx dV = \frac{500\pi}{3}\,\varepsilon + \frac{100\pi}{3}\,\varepsilon = 200\pi\varepsilon .
> $$
>
> The maximum error is about $200\pi\varepsilon$ cm³; for $\varepsilon = 0.1$ it is $20\pi \approx 63$ cm³. Since the measured volume is $\pi (10)^2 (25)/3 \approx 2618$ cm³, this is a relative error of about $63/2618 \approx 2.4\%$.
>
> **(b)** The dimensions of a rectangular box are measured as $75$ cm, $60$ cm and $40$ cm, each correct to within $\varepsilon$ cm. Estimate the largest possible error in the calculated volume, and evaluate it for $\varepsilon = 0.2$.
>
> $V = xyz$, so $dV = yz\,dx + xz\,dy + xy\,dz$ (Definition §93.5). With $dx = dy = dz = \varepsilon$ and $x = 75$, $y = 60$, $z = 40$:
>
> $$
> \Delta V \approx dV = (60)(40)\varepsilon + (75)(40)\varepsilon + (75)(60)\varepsilon = (2400 + 3000 + 4500)\varepsilon = 9900\varepsilon .
> $$
>
> An error of $0.2$ cm in each dimension can lead to an error of about $9900(0.2) = 1980$ cm³ in the volume. That looks large, but the volume is $75 \cdot 60 \cdot 40 = 180{,}000$ cm³, so it is about $1.1\%$.
>
> *Stewart: Examples 14.4.5 and 14.4.6*

^ex-93-4

> [!example] Example §93.5: A Tangent Plane from Two Curves
> Let $S$ be a surface containing the curves
>
> $$
> \mathbf{c}_1(t) = \langle 2 + 3t,\ 1 - t^2,\ 3 - 4t + t^2 \rangle , \qquad \mathbf{c}_2(u) = \langle 1 + u^2,\ 2u^3 - 1,\ 2u + 1 \rangle .
> $$
>
> Find the tangent plane to $S$ at the point $P = (2, 1, 3)$.
>
> **Where the curves pass through $P$.** $\mathbf{c}_1(0) = (2, 1, 3)$. For $\mathbf{c}_2$: $1 + u^2 = 2$ gives $u = \pm 1$, and $2u^3 - 1 = 1$ forces $u = 1$; then $2u + 1 = 3$. So $\mathbf{c}_2(1) = (2, 1, 3)$.
>
> **Tangent vectors** ([[§87 Derivatives and Integrals of Vector Functions#^def-87-2|Definition §87.2]]).
>
> $$
> \mathbf{c}_1'(t) = \langle 3, -2t, -4 + 2t \rangle , \quad \mathbf{c}_1'(0) = \langle 3, 0, -4 \rangle ; \qquad \mathbf{c}_2'(u) = \langle 2u, 6u^2, 2 \rangle , \quad \mathbf{c}_2'(1) = \langle 2, 6, 2 \rangle .
> $$
>
> **Normal vector.** The tangent lines at $P$ to curves on $S$ through $P$ lie in the tangent plane (as noted after Definition §93.1; this is [[§95 Directional Derivatives and the Gradient Vector#^thm-95-5|Theorem §95.5]]), so both tangent vectors are parallel to the plane. They are not parallel to each other, and their cross product ([[§83 The Cross Product#^thm-83-2|Theorem §83.2]]) is a normal vector:
>
> $$
> \langle 3, 0, -4 \rangle \times \langle 2, 6, 2 \rangle = \langle 0 \cdot 2 - (-4) \cdot 6,\ (-4) \cdot 2 - 3 \cdot 2,\ 3 \cdot 6 - 0 \cdot 2 \rangle = \langle 24, -14, 18 \rangle .
> $$
>
> **The plane.**
>
> $$
> 24(x - 2) - 14(y - 1) + 18(z - 3) = 0 , \qquad\text{or}\qquad 12x - 7y + 9z = 44 .
> $$
>
> *Source: 233 Midterm 1 Practice Questions, Q27*

^ex-93-5
