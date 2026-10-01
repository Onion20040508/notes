---
type: section
subject: "[[Calculus]]"
chapter: 9
section: 59
stewart: "9.3"
aliases: ["Stewart 9.3"]
tags: [calculus]
---
← [[§58 Direction Fields and Euler's Method]] · ↑ [[· 9 Differential Equations]] · [[§60 Models for Population Growth]] →

*Stewart, Section 9.3.*

Direction fields and Euler's method ([[§58 Direction Fields and Euler's Method|§58]]) describe solutions of a differential equation geometrically and numerically. For one class of first-order equations an explicit formula is possible: the separable equations, in which $dy/dx$ is a function of $x$ times a function of $y$. Moving all $y$'s to one side and all $x$'s to the other and integrating gives the solutions, sometimes only implicitly. The method covers two standard applications: orthogonal trajectories of a family of curves, and mixing problems, where the amount of a substance in a tank changes at the rate it comes in minus the rate it goes out.

## Separable Differential Equations

> [!definition] Definition §59.1: Separable Equation
> A **separable equation** is a first-order differential equation ([[§57 Modeling with Differential Equations#^def-57-5|Definition §57.5]]) in which the expression for $dy/dx$ factors as a function of $x$ times a function of $y$:
>
> $$
> \frac{dy}{dx} = g(x)\,f(y) .
> $$
>
> The right side can be "separated" into a function of $x$ and a function of $y$. Where $f(y) \ne 0$, the equation can equivalently be written as
>
> $$
> \frac{dy}{dx} = \frac{g(x)}{h(y)}, \qquad h(y) = \frac{1}{f(y)} . \qquad (1)
> $$
>
> *Stewart: 9.3 (text) and Equation 1*

^def-59-1

To solve (1), write it in the **differential form** $h(y)\,dy = g(x)\,dx$, with all $y$'s on one side and all $x$'s on the other, and integrate both sides:

$$
\int h(y)\,dy = \int g(x)\,dx . \qquad (2)
$$

Equation 2 defines $y$ implicitly as a function of $x$; sometimes it can be solved for $y$ in terms of $x$. One constant of integration suffices: constants $C_1$ on the left and $C_2$ on the right combine into $C = C_2 - C_1$. The differential form is notation; the following theorem says what the procedure actually proves. (The technique goes back to James Bernoulli (1690) and Leibniz (1691); John Bernoulli published the general method in 1694.)

> [!theorem] Theorem §59.1: Separation of Variables
> Let $g$ be continuous on an interval $I$ and $h$ continuous on an interval $J$, and let $G$ and $H$ be antiderivatives of $g$ and $h$ ([[§33 Antiderivatives#^def-33-1|Definition §33.1]]). Let $y$ be a differentiable function on an interval $I_0 \subseteq I$ with values in $J$. Then
>
> $$
> h(y)\,\frac{dy}{dx} = g(x) \quad\text{on } I_0
> \qquad\Longleftrightarrow\qquad
> H\big(y(x)\big) = G(x) + C \quad\text{on } I_0 \text{ for some constant } C .
> $$
>
> The right-hand side is Equation 2, $\int h(y)\,dy = \int g(x)\,dx$. Where $h(y) \ne 0$, the left-hand side is Equation 1.
>
> *Stewart: 9.3, Equations 1 and 2 (text)*

^thm-59-1

> [!proof]+ Proof
> ($\Leftarrow$) This is Stewart's justification by the Chain Rule. Suppose $H(y(x)) = G(x) + C$, that is, $\int h(y)\,dy = \int g(x)\,dx$. Differentiate both sides with respect to $x$:
>
> $$
> \frac{d}{dx}\Big(\int h(y)\,dy\Big) = \frac{d}{dx}\Big(\int g(x)\,dx\Big) .
> $$
>
> On the left, $y$ is a function of $x$, so by the Chain Rule ([[§17 The Chain Rule#^thm-17-2|Theorem §17.2]]) the left side is
>
> $$
> \frac{d}{dy}\Big(\int h(y)\,dy\Big)\frac{dy}{dx} = H'(y)\,\frac{dy}{dx} = h(y)\,\frac{dy}{dx} ,
> $$
>
> and the right side is $G'(x) = g(x)$. So $h(y)\,dy/dx = g(x)$, and where $h(y) \ne 0$ this is Equation 1.
>
> ($\Rightarrow$) Stewart does not state this direction, but it is what guarantees that the procedure finds *every* solution. Suppose $h(y)\,y' = g(x)$ on $I_0$ and put $F(x) = H(y(x)) - G(x)$. By the Chain Rule,
>
> $$
> F'(x) = h\big(y(x)\big)\,y'(x) - g(x) = 0 \qquad \text{for all } x \in I_0 .
> $$
>
> A function with zero derivative on an interval is constant (Stewart 4.2, Theorem 5; [[§26 The Mean Value Theorem#^thm-26-3|Theorem §26.3]]), so $F(x) = C$, that is, $H(y(x)) = G(x) + C$.

^pf-59-1

*Uses:* [[§17 The Chain Rule#^thm-17-2|§17.2]] (Chain Rule), [[§26 The Mean Value Theorem#^thm-26-3|§26.3]] (zero derivative on an interval implies constant), [[§33 Antiderivatives#^def-33-1|Def. §33.1]] (antiderivatives)

> [!remark]- Connections
> - The step "zero derivative on an interval implies constant" is proved from the Mean Value Theorem in [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]]. The interval matters: on a domain made of two intervals, $F$ may take a different constant on each piece, which is why a solution is always considered on one interval.

> [!remark] Remark: Method — Solving a Separable Equation
> 1. Write the equation as $dy/dx = g(x)f(y)$ (Definition §59.1).
> 2. Find the **constant solutions**: every number $y_0$ with $f(y_0) = 0$ gives a solution $y \equiv y_0$. Step 3 divides by $f(y)$ and loses them.
> 3. For $f(y) \ne 0$, write $h(y)\,dy = g(x)\,dx$ with $h = 1/f$, and integrate both sides, with one constant $C$ ([[§59 Separable Equations#^thm-59-1|Theorem §59.1]]).
> 4. Solve for $y$ if possible. With $\ln|y|$ or a similar term, exponentiate, and replace $\pm e^{C}$ by one arbitrary constant $A$; often $A = 0$ brings back the constant solution of step 2.
> 5. For an initial-value problem $y(x_0) = y_0$ ([[§57 Modeling with Differential Equations#^def-57-7|Definition §57.7]]), substitute $x_0$ and $y_0$ to find the constant, and state the interval containing $x_0$ on which the formula solves the equation.

^rem-59-1

> [!example] Example §59.1: An Explicit Solution and an Initial-Value Problem
> (a) Solve $\dfrac{dy}{dx} = \dfrac{x^2}{y^2}$. (b) Find the solution with $y(0) = 2$.
>
> **(a)** In differential form, $y^2\,dy = x^2\,dx$. Integrating both sides,
>
> $$
> \int y^2\,dy = \int x^2\,dx \qquad\Longrightarrow\qquad \tfrac13 y^3 = \tfrac13 x^3 + C ,
> $$
>
> where $C$ is an arbitrary constant. Solving for $y$,
>
> $$
> y = \sqrt[3]{x^3 + 3C} = \sqrt[3]{x^3 + K}, \qquad K = 3C .
> $$
>
> Since $C$ is arbitrary, so is $K$.
>
> **(b)** Putting $x = 0$ in the general solution gives $y(0) = \sqrt[3]{K}$. For $y(0) = 2$ we need $\sqrt[3]{K} = 2$, so $K = 8$, and the solution of the initial-value problem is
>
> $$
> y = \sqrt[3]{x^3 + 8} .
> $$
>
> (The equation needs $y \ne 0$. Since $y = 0$ at $x = -2$, where $dy/dx$ would be $4/0$, this formula solves the initial-value problem on the interval $x > -2$, which contains $0$.)
>
> *Stewart: Example 9.3.1*

^ex-59-1

> [!example] Example §59.2: A Solution Given Only Implicitly
> Solve $\dfrac{dy}{dx} = \dfrac{6x^2}{2y + \cos y}$.
>
> In differential form, $(2y + \cos y)\,dy = 6x^2\,dx$. Integrating both sides,
>
> $$
> \int (2y + \cos y)\,dy = \int 6x^2\,dx \qquad\Longrightarrow\qquad y^2 + \sin y = 2x^3 + C , \qquad (3)
> $$
>
> where $C$ is a constant. Equation 3 gives the general solution implicitly. Here it is impossible to solve for $y$ explicitly as a function of $x$. (Check by implicit differentiation, [[§18 Implicit Differentiation|§18]]: $(2y + \cos y)\,y' = 6x^2$.) Software can still plot the curves (3); for each value of $C$ they form one member of the family of solutions.
>
> *Stewart: Example 9.3.2*

^ex-59-2

> [!example] Example §59.3: A Constant Solution and the Constant A
> Solve $y' = x^2 y$.
>
> In Leibniz notation, $\dfrac{dy}{dx} = x^2 y$. The constant function $y = 0$ is a solution: both sides are $0$. If $y \ne 0$, divide by $y$ and integrate:
>
> $$
> \int \frac{dy}{y} = \int x^2\,dx \qquad\Longrightarrow\qquad \ln|y| = \frac{x^3}{3} + C .
> $$
>
> This defines $y$ implicitly, but here we can solve for $y$:
>
> $$
> |y| = e^{\ln|y|} = e^{(x^3/3) + C} = e^{C} e^{x^3/3}, \qquad\text{so}\qquad y = \pm e^{C} e^{x^3/3} .
> $$
>
> (The sign cannot change on an interval: $y$ is continuous and never $0$ there.) Together with $y = 0$, the general solution is
>
> $$
> y = A\,e^{x^3/3} ,
> $$
>
> where $A$ is an arbitrary constant ($A = e^{C}$, $A = -e^{C}$, or $A = 0$).
>
> **Every solution is of this form.** The computation above assumed that a solution is either identically $0$ or never $0$. That can be avoided. If $y' = x^2 y$ on an interval, then
>
> $$
> \frac{d}{dx}\Big(y\,e^{-x^3/3}\Big) = \big(y' - x^2 y\big)\,e^{-x^3/3} = 0 ,
> $$
>
> so $y\,e^{-x^3/3} = A$ is constant (Stewart 4.2, Theorem 5; [[§26 The Mean Value Theorem#^thm-26-3|Theorem §26.3]]) and $y = A\,e^{x^3/3}$. Multiplying by $e^{-x^3/3}$ is the integrating factor of [[§61 Linear Equations#^thm-61-1|Theorem §61.1]].
>
> *Stewart: Example 9.3.3*

^ex-59-3

![[m233-59-1.svg]]
*The direction field of $y' = x^2 y$ (gray) and the solutions $y = Ae^{x^3/3}$ for $A = \pm 3, \pm 1, \pm 0.3$ (blue). The slopes are $0$ along both axes, so every solution has a horizontal tangent at $x = 0$. The constant solution $y = 0$ (red) separates the solutions with $A > 0$ from those with $A < 0$. No solution curve crosses it, or any other solution curve.*

> [!remark]- Connections
> - The integrating factor in 451, as a trick for Rolle's Theorem: [[§29 The Mean Value Theorem#^rem-29-2|451 Remark after Ex. §29.4]]. There $y' + y\,g' = 0$ is written as $(y\,e^{g})' = 0$, exactly the computation above with $g(x) = -x^3/3$.

> [!remark] Remark: Solution Curves Do Not Cross
> Stewart quotes, without proof, a **uniqueness theorem** for equations such as $y' = x^2 y$: if two solutions agree at one value of $x$, they agree at all $x$. So two solution curves are either identical or never intersect. (A standard form: for $y' = F(x, y)$ with $F$ and $\partial F/\partial y$ continuous, an initial-value problem $y(x_0) = y_0$ has only one solution on any interval containing $x_0$. It is proved in a course on differential equations.) In Example §59.3, $y = 0$ is a solution, so every other solution satisfies $y(x) \ne 0$ for all $x$, which is what makes the sign of $\pm e^{C}$ constant.

^rem-59-2

Stewart's Example 4 solves the circuit equation of [[§58 Direction Fields and Euler's Method#^def-58-2|Definition §58.2]] (the circuit of [[§58 Direction Fields and Euler's Method#^ex-58-2|Example §58.2]]) in the same way. With $L = 4$ H, $R = 12\ \Omega$ and a constant voltage $E = 60$ V, $L\,dI/dt + RI = E(t)$ becomes $dI/dt = 15 - 3I$, $I(0) = 0$. Separating, $-\frac13\ln|15 - 3I| = t + C$, so $15 - 3I = Ae^{-3t}$, and $I(0) = 0$ gives $A = 15$: $I(t) = 5 - 5e^{-3t}$. The limiting current is $\lim_{t \to \infty} I(t) = 5$ A.

## Orthogonal Trajectories

> [!definition] Definition §59.2: Orthogonal Trajectory
> An **orthogonal trajectory** of a family of curves is a curve that intersects each curve of the family orthogonally, that is, at right angles: at each intersection point the two tangent lines are perpendicular. Two families are **orthogonal trajectories of each other** if every curve of each family is an orthogonal trajectory of the other family.
>
> For instance, each line $y = mx$ through the origin is an orthogonal trajectory of the family of concentric circles $x^2 + y^2 = r^2$: the radius of a circle is perpendicular to its tangent line. So the lines and the circles are orthogonal trajectories of each other.
>
> *Stewart: 9.3 (text)*

^def-59-2

> [!remark] Remark: Method — Orthogonal Trajectories
> 1. Differentiate the equation of the family (implicitly, [[§18 Implicit Differentiation|§18]]) with respect to $x$.
> 2. Eliminate the parameter of the family, using its equation, to get one differential equation $\dfrac{dy}{dx} = F(x, y)$ that holds for all members at once.
> 3. Perpendicular lines have negative reciprocal slopes ([[§117 Coordinate Geometry and Lines#^thm-117-5|Theorem §117.5]]), so the orthogonal trajectories satisfy $\dfrac{dy}{dx} = -\dfrac{1}{F(x, y)}$.
> 4. Solve this equation, often by separation of variables.

^rem-59-3

> [!example] Example §59.4: Orthogonal Trajectories of Parabolas
> Find the orthogonal trajectories of the family of curves $x = ky^2$, where $k$ is an arbitrary constant.
>
> The curves $x = ky^2$ are parabolas whose axis of symmetry is the $x$-axis. Differentiating $x = ky^2$ with respect to $x$,
>
> $$
> 1 = 2ky\,\frac{dy}{dx} \qquad\text{or}\qquad \frac{dy}{dx} = \frac{1}{2ky} .
> $$
>
> This still depends on $k$. From $x = ky^2$ we have $k = x/y^2$, so
>
> $$
> \frac{dy}{dx} = \frac{1}{2ky} = \frac{1}{2\,\dfrac{x}{y^2}\,y} = \frac{y}{2x} .
> $$
>
> So the tangent line to any of the parabolas at $(x, y)$ has slope $y/(2x)$. On an orthogonal trajectory the slope must be the negative reciprocal:
>
> $$
> \frac{dy}{dx} = -\frac{2x}{y} .
> $$
>
> This equation is separable:
>
> $$
> \int y\,dy = -\int 2x\,dx \qquad\Longrightarrow\qquad \frac{y^2}{2} = -x^2 + C \qquad\Longrightarrow\qquad x^2 + \frac{y^2}{2} = C , \qquad (4)
> $$
>
> where $C$ is an arbitrary positive constant. The orthogonal trajectories are the ellipses (4), centered at the origin, with semi-axes $\sqrt{C}$ along the $x$-axis and $\sqrt{2C}$ along the $y$-axis.
>
> *Stewart: Example 9.3.5*

^ex-59-4

![[m233-59-2.svg]]
*The parabolas $x = ky^2$ (blue, $k = \pm\frac14, \pm\frac12, \pm 1, \pm 2$) and their orthogonal trajectories, the ellipses $x^2 + \frac12 y^2 = C$ (red). At the marked point $(\frac12, 1)$ the parabola $k = \frac12$ has slope $y/(2x) = 1$ and the ellipse $C = \frac34$ has slope $-2x/y = -1$, so they meet at a right angle.*

Orthogonal trajectories occur in several branches of physics. In an electrostatic field the lines of force are orthogonal to the lines of constant potential. In aerodynamics the streamlines are orthogonal trajectories of the velocity-equipotential curves.

## Mixing Problems

In a typical **mixing problem**, a tank of fixed capacity holds a thoroughly mixed solution of some substance, such as salt. A solution of a given concentration enters the tank at a fixed rate, and the mixture, thoroughly stirred, leaves at a fixed rate, which may differ from the rate in. If $y(t)$ is the amount of the substance in the tank at time $t$, then $y'(t)$ is the rate at which the substance is added minus the rate at which it is removed:

$$
\frac{dy}{dt} = (\text{rate in}) - (\text{rate out}) . \qquad (5)
$$

This often leads to a first-order separable equation. The same reasoning models chemical reactions, the discharge of pollutants into a lake, and the injection of a drug into the bloodstream.

> [!remark] Remark: Method — Mixing Problems
> 1. Let $y(t)$ be the amount of the substance, and record $y(0)$.
> 2. Rate in $=$ (concentration of the incoming solution) $\times$ (inflow rate).
> 3. Rate out $=$ (concentration in the tank) $\times$ (outflow rate), where the concentration in the tank is $y(t)$ divided by the volume of liquid in the tank at time $t$ (constant when inflow and outflow rates are equal).
> 4. Form Equation 5, solve it with the initial condition, and evaluate at the time asked for. Keep track of units: if amounts are in kg, volumes in L and time in min, all terms of (5) are in kg/min.

^rem-59-4

> [!example] Example §59.5: Salt in a Tank
> A tank contains $20$ kg of salt dissolved in $5000$ L of water. Brine that contains $0.03$ kg of salt per liter of water enters the tank at a rate of $25$ L/min. The solution is kept thoroughly mixed and drains from the tank at the same rate. How much salt is in the tank after half an hour?
>
> Let $y(t)$ be the amount of salt (in kg) after $t$ minutes. Then $y(0) = 20$, and we want $y(30)$. By Equation 5, $dy/dt = (\text{rate in}) - (\text{rate out})$, where
>
> $$
> \text{rate in} = \Big(0.03\ \frac{\text{kg}}{\text{L}}\Big)\Big(25\ \frac{\text{L}}{\text{min}}\Big) = 0.75\ \frac{\text{kg}}{\text{min}} .
> $$
>
> The tank always contains $5000$ L of liquid, so the concentration at time $t$ is $y(t)/5000$ kg/L, and
>
> $$
> \text{rate out} = \Big(\frac{y(t)}{5000}\ \frac{\text{kg}}{\text{L}}\Big)\Big(25\ \frac{\text{L}}{\text{min}}\Big) = \frac{y(t)}{200}\ \frac{\text{kg}}{\text{min}} .
> $$
>
> Thus
>
> $$
> \frac{dy}{dt} = 0.75 - \frac{y(t)}{200} = \frac{150 - y(t)}{200} .
> $$
>
> Separating variables,
>
> $$
> \int \frac{dy}{150 - y} = \int \frac{dt}{200} \qquad\Longrightarrow\qquad -\ln|150 - y| = \frac{t}{200} + C .
> $$
>
> Since $y(0) = 20$, $-\ln 130 = C$, so
>
> $$
> -\ln|150 - y| = \frac{t}{200} - \ln 130 \qquad\Longrightarrow\qquad |150 - y| = 130\,e^{-t/200} .
> $$
>
> Since $y(t)$ is continuous, $y(0) = 20$, and the right side is never $0$, the quantity $150 - y(t)$ never changes sign, so it is always positive. Thus $|150 - y| = 150 - y$ and
>
> $$
> y(t) = 150 - 130\,e^{-t/200} .
> $$
>
> The amount of salt after $30$ min is
>
> $$
> y(30) = 150 - 130\,e^{-30/200} = 150 - 130\,e^{-0.15} \approx 38.1\ \text{kg} .
> $$
>
> As $t \to \infty$, $y(t) \to 150$ kg. This is $0.03 \times 5000$: in the long run the tank has the concentration of the incoming brine.
>
> *Stewart: Example 9.3.6*

^ex-59-5
