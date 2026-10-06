---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 5
bdp: "2.2"
aliases: ["BDP 2.2"]
tags: [ordinary-differential-equations, math331]
---
← [[§4 Linear Differential Equations; Method of Integrating Factors]] · ↑ [[· 2 First-Order Differential Equations]] · [[§6 Modeling with First-Order Differential Equations]] →

*Boyce–DiPrima, Section 2.2 · MATH 331 Written HW 1 (Problems 1 and 3), Midterms Fall 2021 (Q2), Spring 2020 (Q2) and Summer 2023 (Q2).*

The direct integration of [[§2 Solutions of Some Differential Equations|§2]] works for a much larger class of equations, most of them nonlinear: the separable equations $M(x) + N(y)\,dy/dx = 0$, in which the variables can be put on opposite sides. Integrating each side gives an equation $H_1(x) + H_2(y) = c$ that defines the solutions implicitly. Two new features appear that linear equations did not have. The solution is often only implicit, and solving for $y$ may be impossible. And the interval on which a solution exists depends on the initial value, not just on the coefficients; it ends where the integral curve has a vertical tangent or the solution blows up. A change of variable extends the method to homogeneous equations $dy/dx = F(y/x)$. In this section the independent variable is $x$.

## Separable Equations

The general first-order equation $dy/dx = f(x, y)$ can always be written as
$$
M(x, y) + N(x, y)\,\frac{dy}{dx} = 0 \qquad (3)
$$
(for instance with $M = -f$, $N = 1$), and often in other ways too.

> [!definition] Definition §5.1: Separable Equation
> The equation (3) is **separable** if $M$ is a function of $x$ only and $N$ is a function of $y$ only:
>
> $$
> M(x) + N(y)\,\frac{dy}{dx} = 0 . \qquad (4)
> $$
>
> Written in the **differential form**
>
> $$
> M(x)\,dx + N(y)\,dy = 0 , \qquad (5)
> $$
>
> the terms involving each variable can be placed on opposite sides of the equation. The differential form is more symmetric and tends to suppress the distinction between the independent and the dependent variable.
>
> *BDP: 2.2 (text)*

^def-5-1

For example, $\dfrac{dy}{dx} = \dfrac{x^2}{1 - y^2}$ is separable, since it can be written $-x^2 + (1 - y^2)\,\dfrac{dy}{dx} = 0$. By the chain rule the second term is $\dfrac{d}{dx}\big(y - \tfrac{y^3}{3}\big)$ and the first is $\dfrac{d}{dx}\big(-\tfrac{x^3}{3}\big)$, so the equation says $\dfrac{d}{dx}\big(-\tfrac{x^3}{3} + y - \tfrac{y^3}{3}\big) = 0$, and its integral curves are $-x^3 + 3y - y^3 = c$ (BDP, Example 2.2.1). The theorem below is the same argument in general.

> [!theorem] Theorem §5.1: Solution of a Separable Equation
> Let $M$ be continuous on an interval $I$ and $N$ continuous on an interval $J$, and let $H_1$ and $H_2$ be antiderivatives of $M$ and $N$:
>
> $$
> H_1'(x) = M(x) , \qquad H_2'(y) = N(y) . \qquad (9)
> $$
>
> A differentiable function $y = \phi(x)$ on an interval $I_0 \subseteq I$, with values in $J$, is a solution of (4) on $I_0$ if and only if
>
> $$
> H_1(x) + H_2\big(\phi(x)\big) = c \quad \text{on } I_0 \qquad (13)
> $$
>
> for some constant $c$. Thus (13) defines the solutions **implicitly**. The solution with $y(x_0) = y_0$ satisfies
>
> $$
> \int_{x_0}^{x} M(s)\,ds + \int_{y_0}^{y} N(s)\,ds = 0 . \qquad (16)
> $$
>
> In practice, (13) is obtained from the differential form (5) by integrating the first term with respect to $x$ and the second with respect to $y$; the theorem is the justification for doing so.
>
> *BDP: 2.2, Equations (9)–(16) (text)*

^thm-5-1

> [!proof]+ Proof
> **($\Rightarrow$)** Let $\phi$ be a solution on $I_0$, so $H_1'(x) + H_2'(\phi(x))\,\phi'(x) = 0$ by (9) and (4). By the chain rule,
>
> $$
> H_2'\big(\phi(x)\big)\,\phi'(x) = \frac{d}{dx}H_2\big(\phi(x)\big) , \qquad (11)
> $$
>
> so (4) becomes
>
> $$
> \frac{d}{dx}\Big[H_1(x) + H_2\big(\phi(x)\big)\Big] = 0 . \qquad (12)
> $$
>
> A function with zero derivative on the interval $I_0$ is constant, which is (13). (BDP says "integrating (12)".)
>
> **($\Leftarrow$)** BDP asserts that any differentiable $\phi$ satisfying (13) is a solution; here is why. Differentiating (13) with the chain rule gives $M(x) + N(\phi(x))\,\phi'(x) = 0$ on $I_0$, which is (4).
>
> **The initial value problem.** Setting $x = x_0$, $\phi(x_0) = y_0$ in (13) gives
>
> $$
> c = H_1(x_0) + H_2(y_0) . \qquad (15)
> $$
>
> Substituting this into (13), and using $H_1(x) - H_1(x_0) = \int_{x_0}^{x} M(s)\,ds$ and $H_2(y) - H_2(y_0) = \int_{y_0}^{y} N(s)\,ds$ (Fundamental Theorem of Calculus, [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]), gives (16).

^pf-5-1

*Uses:* [[§5 Separable Differential Equations#^def-5-1|Def. §5.1]], [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]] (zero derivative on an interval), [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]] (FTC I)

> [!remark]- Connections
> - See also: [[§59 Separable Equations#^def-59-1|Calc Def. §59.1]] and [[§59 Separable Equations#^thm-59-1|Calc Thm. §59.1]] (Stewart's treatment, in the form $h(y)\,dy/dx = g(x)$) and its [[§59 Separable Equations#^rem-59-1|Calc Remark: Method — Solving a Separable Equation]].
> - When does (16) actually define $y$ as a differentiable function of $x$? Put $F(x, y) = \int_{x_0}^{x} M + \int_{y_0}^{y} N$. Then $F_y = N(y)$, and if $N(y_0) \ne 0$ the [[§12 The Implicit Function Theorem#^thm-12-1|452 Thm. §12.1]] (Implicit Function Theorem) gives a unique differentiable $\phi$ near $x_0$ with $F(x, \phi(x)) = 0$ and $\phi' = -F_x/F_y = -M/N$, which is (4). Where $N(y) = 0$ the integral curve can have a vertical tangent, and the solution ends there ([[§5 Separable Differential Equations#^ex-5-1|Examples §5.1]] and [[§5 Separable Differential Equations#^ex-5-2|§5.2]]). The generalization to $M(x, y)\,dx + N(x, y)\,dy = 0$ is the exact equations of [[§9 Exact Differential Equations and Integrating Factors#^def-9-1|Definition §9.1]].

> [!remark] Remark: Method — Separation of Variables
> 1. **Separate.** Write the equation as $N(y)\,dy = M(x)\,dx$ (move all $y$'s to one side and all $x$'s to the other). If you divide by an expression in $y$, record its zeros $y_0$: if $f(x, y_0) = 0$ for all $x$, the constant function $y = y_0$ is a solution that the division loses ([[§5 Separable Differential Equations#^rem-5-2|Remark: Constant Solutions]] below).
> 2. **Integrate** both sides, with a single constant: $H_2(y) = H_1(x) + c$.
> 3. **Initial condition.** Substitute $x_0$, $y_0$ to find $c$ (it is easiest to do this before solving for $y$).
> 4. **Solve for $y$** if convenient; if the equation for $y$ has several roots (a $\pm$ sign), keep the one that passes through $(x_0, y_0)$. Otherwise leave the solution implicit.
> 5. **Interval of validity.** The solution extends on either side of $x_0$ as long as it stays differentiable: it ends where it blows up, where a square root or logarithm becomes undefined, or where the integral curve has a vertical tangent ($N(y) = 0$).

^rem-5-1

> [!example] Example §5.1: An Explicit Solution and Its Interval
> Solve the initial value problem
>
> $$
> \frac{dy}{dx} = \frac{3x^2 + 4x + 2}{2(y - 1)} , \qquad y(0) = -1 , \qquad (17)
> $$
>
> and determine the interval in which the solution exists.
>
> **Separate and integrate.** $2(y - 1)\,dy = (3x^2 + 4x + 2)\,dx$, so
>
> $$
> y^2 - 2y = x^3 + 2x^2 + 2x + c . \qquad (18)
> $$
>
> **Initial condition.** $x = 0$, $y = -1$: $1 + 2 = c$, so $c = 3$ and $y^2 - 2y = x^3 + 2x^2 + 2x + 3$.
>
> **Solve for $y$.** The equation is quadratic in $y$: $(y - 1)^2 = x^3 + 2x^2 + 2x + 4$, so
>
> $$
> y = 1 \pm \sqrt{x^3 + 2x^2 + 2x + 4} . \qquad (20)
> $$
>
> At $x = 0$ the root is $\sqrt4 = 2$, and $y(0) = -1 = 1 - 2$ requires the minus sign:
>
> $$
> y = \phi(x) = 1 - \sqrt{x^3 + 2x^2 + 2x + 4} . \qquad (21)
> $$
>
> (The plus sign gives the solution of the same equation with $y(0) = 3$.)
>
> **Interval.** The solution is differentiable where the quantity under the root is positive. It factors as $x^3 + 2x^2 + 2x + 4 = (x + 2)(x^2 + 2)$, whose only real zero is $x = -2$, so the interval is $x > -2$. At the boundary point $(-2, 1)$ we have $y = 1$, where the right side of (17) has a zero denominator: the integral curve has a vertical tangent there.
>
> *BDP: Example 2.2.2*

^ex-5-1

> [!example] Example §5.2: A Solution Given Only Implicitly
> Solve $\dfrac{dy}{dx} = \dfrac{4x - x^3}{4 + y^3}$, find the solution through $(0, 1)$, and determine its interval of validity.
>
> **Separate and integrate.** $(4 + y^3)\,dy = (4x - x^3)\,dx$ gives $4y + \frac{y^4}{4} = 2x^2 - \frac{x^4}{4} + C$; multiplying by $4$ and rearranging,
>
> $$
> y^4 + 16y + x^4 - 8x^2 = c . \qquad (23)
> $$
>
> Any differentiable $y = \phi(x)$ satisfying (23) is a solution. Solving the quartic for $y$ is not worth attempting.
>
> **Through $(0, 1)$.** $1 + 16 + 0 - 0 = c$, so $c = 17$:
>
> $$
> y^4 + 16y + x^4 - 8x^2 = 17 . \qquad (24)
> $$
>
> **Interval.** The solution extends on either side of $x = 0$ as long as it stays differentiable, which fails where the tangent becomes vertical: where the denominator $4 + y^3 = 0$, that is, $y = -4^{1/3} \approx -1.5874$. There $y^3 = -4$, so $y^4 = -4y$ and $y^4 + 16y = 12y \approx -19.049$. Then (24) gives
>
> $$
> x^4 - 8x^2 - (17 + 19.049) = 0 , \qquad x^2 = 4 + \sqrt{16 + 36.049} \approx 11.2145 , \qquad x \approx \pm 3.3488 .
> $$
>
> The solution through $(0, 1)$ exists on $-3.3488 < x < 3.3488$, approximately.
>
> *BDP: Example 2.2.3*

^ex-5-2

![[m331-5-1.svg]]
*Integral curves $y^4 + 16y + x^4 - 8x^2 = c$ of [[§5 Separable Differential Equations#^ex-5-2|Example §5.2]] (blue, $c = -20, -8, 4, 30, 45$). The level curve $c = 17$ is a closed curve, but only its upper arc (green) is the solution through $(0, 1)$: it ends at the two points $(\pm 3.3488, -1.5874)$ on the line $y = -4^{1/3}$ (dashed), where every integral curve has a vertical tangent. The lower arc (pale green) is a different solution of the same equation.*

> [!remark] Remark: Constant Solutions
> If $f(x, y_0) = 0$ for some $y_0$ and all $x$, then the constant function $y = y_0$ is a solution of $dy/dx = f(x, y)$, since both sides are $0$. Such solutions are easy to find and easy to lose: separating the variables divides by an expression that vanishes at $y_0$. For example, $\dfrac{dy}{dx} = \dfrac{(y - 3)\cos x}{1 + 2y^2}$ has the constant solution $y = 3$; the other solutions are found by separating variables.

^rem-5-2

> [!remark] Remark: Implicit Solutions and Parametrization
> - In [[§5 Separable Differential Equations#^ex-5-1|Example §5.1]] it was easy to solve for $y$, but that is exceptional. BDP's convention: "solve the differential equation" means find the solution explicitly if convenient, and otherwise an equation defining it implicitly.
> - Sometimes it helps to regard both $x$ and $y$ as functions of a third variable $t$. Then $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$, and an equation $\dfrac{dy}{dx} = \dfrac{F(x, y)}{G(x, y)}$ is matched by the system $\dfrac{dx}{dt} = G(x, y)$, $\dfrac{dy}{dt} = F(x, y)$. Replacing one equation by two may seem a step backward, but systems of this form are often easier to investigate; Chapter 7 begins their study ([[§27 Introduction to Systems of First-Order Linear Equations|§27]]).

^rem-5-3

> [!example] Example §5.3: Partial Fractions and Blow-Up
> Solve the initial value problem $\dfrac{dy}{dt} = 4y(y + 2)$, $y(0) = 6$, and find the interval on which the solution exists.
>
> **Constant solutions.** The right side vanishes for $y = 0$ and $y = -2$, so these are constant solutions. Ours starts at $6$, so $y \ne 0, -2$ near $t = 0$ and we may divide.
>
> **Separate.** $\dfrac{dy}{y(y + 2)} = 4\,dt$. Partial fractions: $\dfrac{1}{y(y + 2)} = \dfrac12\Big(\dfrac1y - \dfrac{1}{y + 2}\Big)$, so
>
> $$
> \frac12\big(\ln|y| - \ln|y + 2|\big) = 4t + C , \qquad \ln\Big|\frac{y}{y + 2}\Big| = 8t + 2C , \qquad \frac{y}{y + 2} = Ke^{8t} .
> $$
>
> **Initial condition.** At $t = 0$: $K = \frac{6}{8} = \frac34$.
>
> **Solve for $y$.** $y = \frac34 e^{8t}(y + 2)$ gives $y\big(1 - \frac34 e^{8t}\big) = \frac32 e^{8t}$, so
>
> $$
> y = \frac{\frac32 e^{8t}}{1 - \frac34 e^{8t}} = \frac{6}{4e^{-8t} - 3} .
> $$
>
> **Check.** $y(0) = 6/(4 - 3) = 6$, and $y' = \dfrac{192e^{-8t}}{(4e^{-8t} - 3)^2}$, while $4y(y + 2) = \dfrac{24}{4e^{-8t} - 3} \cdot \dfrac{8e^{-8t}}{4e^{-8t} - 3}$, the same.
>
> **Interval.** The denominator vanishes when $e^{-8t} = \frac34$, that is, at $t^{\ast} = \frac18\ln\frac43 \approx 0.036$. So the solution exists on $-\infty < t < \frac18\ln\frac43$: it blows up to $+\infty$ after a very short time, although the right side $4y(y + 2)$ is a polynomial, defined and smooth everywhere. As $t \to -\infty$, $y \to 0$. This is a typically nonlinear phenomenon: for a linear equation the solution exists wherever the coefficients are continuous ([[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]]), while for $y' = y^2$ the blow-up time depends on the initial value ([[§7 Differences Between Linear and Nonlinear Differential Equations#^ex-7-4|Example §7.4]]).
>
> *Source: 331 Written HW 1, Problem 1*

^ex-5-3

> [!example] Example §5.4: Three Exam Problems of the Form y′ = g(x)y²
> **(a)** Find the explicit solution of $\dfrac{dy}{dx} = -6e^{3x}y^2$, $y(0) = 3$.
>
> The constant function $y = 0$ is a solution; ours has $y(0) = 3 \ne 0$. Separate: $y^{-2}\,dy = -6e^{3x}\,dx$, so
>
> $$
> -\frac1y = -2e^{3x} + C .
> $$
>
> At $x = 0$: $-\frac13 = -2 + C$, so $C = \frac53$. Then $\frac1y = 2e^{3x} - \frac53$ and
>
> $$
> y = \frac{3}{6e^{3x} - 5} .
> $$
>
> Check: $y' = -\dfrac{54e^{3x}}{(6e^{3x} - 5)^2} = -6e^{3x}\cdot\dfrac{9}{(6e^{3x} - 5)^2} = -6e^{3x}y^2$. The solution exists while $6e^{3x} > 5$, that is, for $x > \frac13\ln\frac56 \approx -0.061$; it blows up as $x$ decreases to that value, and tends to $0$ as $x \to \infty$.
>
> **(b)** Find the explicit solution of $\dfrac{dy}{dx} = -6xy^2 + 2y^2$, $y(0) = 1$.
>
> Factor: $\dfrac{dy}{dx} = y^2(2 - 6x)$. Separate: $y^{-2}\,dy = (2 - 6x)\,dx$, so $-\dfrac1y = 2x - 3x^2 + C$ and $y = \dfrac{1}{3x^2 - 2x - C}$. At $x = 0$: $1 = -\frac1C$, so $C = -1$ and
>
> $$
> y = \frac{1}{3x^2 - 2x + 1} .
> $$
>
> Here the denominator has discriminant $4 - 12 < 0$, so it is never $0$: this solution exists for all $x$.
>
> **(c)** Solve $\dfrac{dy}{dx} = x^5y^2 + 4xy^2$, $y(0) = 1$.
>
> Factor: $\dfrac{dy}{dx} = y^2(x^5 + 4x)$. Again $y = 0$ is a constant solution and ours starts at $1$. Separate: $y^{-2}\,dy = (x^5 + 4x)\,dx$, so
>
> $$
> -\frac1y = \frac{x^6}{6} + 2x^2 + C .
> $$
>
> At $x = 0$: $-1 = C$. Then $\frac1y = 1 - \frac{x^6}{6} - 2x^2$ and
>
> $$
> y = \frac{6}{6 - x^6 - 12x^2} .
> $$
>
> Check: with $D = 6 - x^6 - 12x^2$, $y' = -\dfrac{6D'}{D^2} = \dfrac{36x(x^4 + 4)}{D^2} = (x^5 + 4x)\cdot\dfrac{36}{D^2} = (x^5 + 4x)\,y^2$. The denominator is $6$ at $x = 0$ and decreases as $|x|$ grows. With $u = x^2$ it vanishes where $u^3 + 12u - 6 = 0$; the left side is increasing in $u$, so there is exactly one root, $u^* = \sqrt[3]{3 + \sqrt{73}} - \sqrt[3]{\sqrt{73} - 3} \approx 0.4902$ (Cardano's formula). So the solution exists on $|x| < \sqrt{u^*} \approx 0.7001$ and blows up at both ends.
>
> The three problems look alike, but the interval of existence depends on the data, not on the form of the equation: the solution in (a) blows up on one side, the one in (b) exists for all $x$, and the one in (c) blows up on both sides. How the interval in (a) moves with the initial value is worked out in [[§7 Differences Between Linear and Nonlinear Differential Equations#^ex-7-4|Example §7.4]](b).
>
> *Source: 331 Midterm (Fall 2021), Q2*
> *Source: 331 Midterm (Spring 2020), Q2*
> *Source: 331 Midterm (Summer 2023), Q2*

^ex-5-4

## Homogeneous Equations

> [!definition] Definition §5.2: Homogeneous Equation
> The equation $dy/dx = f(x, y)$ is **homogeneous** if its right side can be expressed as a function of the ratio $y/x$ only:
>
> $$
> \frac{dy}{dx} = F\Big(\frac{y}{x}\Big) .
> $$
>
> For example, $\dfrac{dy}{dx} = \dfrac{y - 4x}{x - y} = \dfrac{(y/x) - 4}{1 - (y/x)}$ is homogeneous. The word has nothing to do with the homogeneous linear equations of Chapter 3 ([[§13 Homogeneous Differential Equations with Constant Coefficients|§13]]).
>
> *BDP: 2.2 (text before Problem 2.2.25)*

^def-5-2

> [!theorem] Proposition §5.2: Homogeneous Equations Become Separable
> If $\dfrac{dy}{dx} = F\Big(\dfrac yx\Big)$, then the new dependent variable $v = y/x$, that is, $y = x\,v(x)$, satisfies the separable equation
>
> $$
> x\,\frac{dv}{dx} = F(v) - v .
> $$
>
> *BDP: Problem 2.2.25*

^prop-5-2

> [!proof]+ Proof
> On an interval where $x \ne 0$, $y = xv$ by the product rule gives $\dfrac{dy}{dx} = v + x\,\dfrac{dv}{dx}$. Substituting this and $y/x = v$ into the equation gives $v + x\,\dfrac{dv}{dx} = F(v)$, that is, $x\,\dfrac{dv}{dx} = F(v) - v$. In the form $\dfrac{dv}{F(v) - v} = \dfrac{dx}{x}$ (where $F(v) \ne v$) it is separable ([[§5 Separable Differential Equations#^def-5-1|Definition §5.1]]). For the example above, $F(v) - v = \dfrac{v - 4}{1 - v} - v = \dfrac{v^2 - 4}{1 - v}$.

^pf-5-2

*Uses:* [[§5 Separable Differential Equations#^def-5-1|Def. §5.1]], [[§5 Separable Differential Equations#^def-5-2|Def. §5.2]]

Because $f$ depends only on $y/x$, integral curves have the same slope at all points of each line through the origin, so the direction field and the integral curves of a homogeneous equation are symmetric with respect to the origin.

> [!example] Example §5.5: A Homogeneous Equation
> Find the general solution of $y' = \dfrac yx - 2e^{5y/x}$.
>
> **Substitute.** The right side is $F(y/x)$ with $F(v) = v - 2e^{5v}$, so the equation is homogeneous. With $y = xv$, [[§5 Separable Differential Equations#^prop-5-2|Proposition §5.2]] gives
>
> $$
> v + x\,\frac{dv}{dx} = v - 2e^{5v} , \qquad x\,\frac{dv}{dx} = -2e^{5v} .
> $$
>
> The right side never vanishes, so there are no constant solutions $v =$ const.
>
> **Separate and integrate.** $e^{-5v}\,dv = -\dfrac{2}{x}\,dx$, so
>
> $$
> -\frac15 e^{-5v} = -2\ln|x| + C , \qquad e^{-5v} = 10\ln|x| + C' \quad (C' = -5C) .
> $$
>
> **Solve.** Taking logarithms, $v = -\frac15\ln\big(10\ln|x| + C'\big)$, and returning to $y = xv$:
>
> $$
> y = -\frac{x}{5}\,\ln\big(10\ln|x| + C\big) ,
> $$
>
> renaming the constant $C$. It is valid on intervals where $x \ne 0$ and $10\ln|x| + C > 0$ (as it must be, being equal to $e^{-5v} > 0$).
>
> **Check.** With $y/x = v$ and $L = 10\ln|x| + C$: $y' = v + xv'$ and $v' = -\frac15\cdot\frac{10/x}{L} = -\frac{2}{xL}$, so $y' = v - \frac2L$. Since $e^{5v} = e^{-\ln L} = \frac1L$, this is $v - 2e^{5v} = \frac yx - 2e^{5y/x}$.
>
> *Source: 331 Written HW 1, Problem 3*

^ex-5-5

> [!remark] Remark: Method — Homogeneous Equations
> 1. Check that $dy/dx = f(x, y)$ can be written as $F(y/x)$ (for a quotient of polynomials, divide numerator and denominator by the highest power of $x$).
> 2. Substitute $y = xv$, $dy/dx = v + x\,dv/dx$.
> 3. Solve the separable equation $x\,dv/dx = F(v) - v$ for $v$ (implicitly if necessary), noting any constant solutions $F(v_0) = v_0$, which give the lines $y = v_0x$.
> 4. Replace $v$ by $y/x$.

^rem-5-4
